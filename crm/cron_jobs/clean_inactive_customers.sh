#!/bin/bash

# Absolute paths (VERY important for cron)
PROJECT_DIR="/alx_travel_app"
PYTHON="$PROJECT_DIR/venv/bin/python"
MANAGE="$PROJECT_DIR/manage.py"
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Run Django shell command
DELETED_COUNT=$($PYTHON $MANAGE shell -c "
from crm.models import Customer
from django.utils import timezone
from datetime import timedelta

one_year_ago = timezone.now() - timedelta(days=365)

qs = Customer.objects.filter(
    orders__isnull=True,
    created_at__lt=one_year_ago
)

count = qs.count()
qs.delete()
print(count)
")

# Log output with timestamp
echo \"$(date '+%Y-%m-%d %H:%M:%S') - Deleted customers: $DELETED_COUNT\" >> $LOG_FILE
