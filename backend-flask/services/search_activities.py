from datetime import datetime, timedelta, timezone
#Honeycomb
from opentelemetry import trace
tracer = trace.get_tracer("search.activities")
class SearchActivities:
  def run(search_term):
    with tracer.start_as_current_span("show.activities.mock.data"):  
      span = trace.get_current_span()
      model = {
        'errors': None,
        'data': None
      }

      now = datetime.now(timezone.utc).astimezone()

      if search_term == None or len(search_term) < 1:
        model['errors'] = ['search_term_blank']
      else:
        results = [{
          'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          'handle':  'Andrew Brown',
          'message': 'Cloud is fun!',
          'created_at': now.isoformat()
        }]
        model['data'] = results
      span.set_attribute("search.activities.user.id",[d.get('handle', None) for d in results])
      span.set_attribute("search.activities.search.term",search_term)
      span.set_attribute("search.activities.search.term.lenght",len(search_term))
      return model