

## GIT LFS

```bash
git lfs install
git lfs track '*.tar*'
git config http.sslverify false
git config lfs.contenttype false
```

Setting `sslverify` to false helps if uploading to a server without CA cert.
Meanwhile, setting `contenttype` to false helps in temporarily fix a bug in lfs, and prevent for git to figure out best method for data upload.

Thereafter, use git as usual.
