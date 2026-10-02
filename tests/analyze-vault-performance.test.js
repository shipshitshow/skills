const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {execFileSync, spawnSync} = require('node:child_process');
const script = path.resolve(__dirname, '../youtube-metadata/scripts/analyze-vault-performance.js');
test('includes every format and treats absent views as unknown', () => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'show-vault-'));
  try {
    for (const [folder, title, views] of [
      ['shipshitshow/Livestreams/2026-09-29-id', 'Compare models', ''],
      ['shipshitshow/Videos/2026-10-01-id', 'Why this workflow?', 'view_count: "42"\n'],
      ['shipshitshowclips/Shorts/unknown-date/short-id', 'Define done', 'view_count: "0"\n']
    ]) {
      const dir = path.join(root, folder); fs.mkdirSync(dir, {recursive:true});
      fs.writeFileSync(path.join(dir, 'overview.md'), `---\ntitle: "${title}"\ndate: "2026-10-01"\n${views}---\n`);
    }
    const report = JSON.parse(execFileSync(process.execPath, [script, '--vault', root, '--channel', 'all'], {encoding:'utf8'}));
    assert.equal(report.channels.livestreams.count, 1);
    assert.equal(report.channels.videos.count, 1);
    assert.equal(report.channels.shorts.count, 1);
    assert.equal(report.channels.livestreams.averageViews, null);
    assert.equal(report.channels.shorts.averageViews, 0);
    assert.equal(report.channels.videos.averageViews, 42);
    assert.equal(report.channels.livestreams.entriesWithViewSnapshot, 0);
    assert.equal(report.channels.videos.recentExamples.length, 1);
  } finally { fs.rmSync(root, {recursive:true, force:true}); }
});
test('rejects invalid format selection rather than silently selecting Shorts', () => {
  const result = spawnSync(process.execPath, [script, '--channel', 'typo'], {encoding:'utf8'});
  assert.notEqual(result.status, 0);
});
