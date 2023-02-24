from datetime import datetime, timedelta, timezone
class HealthChecker:
  def run():
    now = datetime.now(timezone.utc).astimezone()
    results = [{
      'uuid': '68f126b0-1ceb-4a33-88be-d90fa7109eee',
      'message': 'backend is up!',
      'success': True,
      'created_at': (now - timedelta(days=2)).isoformat(),
    }
    
    ]
    return results