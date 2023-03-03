from datetime import datetime, timedelta, timezone
#Honeycomb
from opentelemetry import trace
tracer = trace.get_tracer("messagegroups")

class MessageGroups:
  def run(user_handle):
    with tracer.start_as_current_span("messagegroups.mock.data"):  
      span = trace.get_current_span()
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()
      results = [
        {
          'uuid': '24b95582-9e7b-4e0a-9ad1-639773ab7552',
          'display_name': 'Andrew Brown',
          'handle':  'andrewbrown',
          'created_at': now.isoformat()
        },
        {
          'uuid': '417c360e-c4e6-4fce-873b-d2d71469b4ac',
          'display_name': 'Worf',
          'handle':  'worf',
          'created_at': now.isoformat()
      }]
      model['data'] = results
      span.set_attribute("messagegroups.user.id",[d.get('handle', None) for d in results])
      span.set_attribute("messagegroups.count",len(results))
      return model