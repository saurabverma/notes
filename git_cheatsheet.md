# GIT LFS

Store the lfs files on a different branch, which is not checkout unless those specific lfs files are required.
Once the specific branch with lfs files is checkout, the relevant lfs files are then downloaded.

## Install (Ubuntu 16.04 or earlier)

```bash
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
```


## Setup

Use `*` to capture all file names with a specific type or all files in a directory.

```bash
git lfs install
git lfs track '*.tar*'
git config http.sslverify false
git config lfs.contenttype false
```

Setting `sslverify` to false helps if uploading to a server without CA cert.
Meanwhile, setting `contenttype` to false helps in temporarily fix a bug in lfs, and prevent for git to figure out best method for data upload.

Thereafter, use git as usual.

## Check

After git commit, check which actual files are in lfs track using `git lfs ls-files`.
