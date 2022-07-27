#!/bin/bash
set -e

sleep 10

exec celery -A project worker -l INFO --concurrency=2