# couchbase-backups-s3

###What?

Simple python script to backup couchbase buckets using cbbbackup tool and upload to S3

###What do you need? 
- an `S3` bucket to store pem key and python scripts
- an `S3` bucket to upload backups
- `AWS CLI` on each node with proper access to target s3 bucket
- Paramiko library

###How?
Download `couch-backup.py` and `master-couch.py`. Schedule couch-backup.py as a job. 

This script makes sure that you can continue taking backups even if the cluster definition changes as long as the specified node in the script is up and running. 

For more details, please visit [this post](http://blog.powerupcloud.com/2016/03/26/automating-couchbase-backups-backup-to-s3/) on our blog. 
