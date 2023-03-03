import { WebTracerProvider } from '@opentelemetry/sdk-trace-web';
import { getWebAutoInstrumentations } from '@opentelemetry/auto-instrumentations-web';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { BatchSpanProcessor } from '@opentelemetry/sdk-trace-base';
import { registerInstrumentations } from '@opentelemetry/instrumentation';
import { ZoneContextManager } from '@opentelemetry/context-zone';
import { DocumentLoadInstrumentation } from '@opentelemetry/instrumentation-document-load';
import { UserInteractionInstrumentation } from '@opentelemetry/instrumentation-user-interaction';
import { LongTaskInstrumentation } from '@opentelemetry/instrumentation-long-task';


const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const exporter = new OTLPTraceExporter({
 url: 'https://api.honeycomb.io/v1/traces',
 headers: {
  "x-honeycomb-team": "bNOlJUSUx5uqOaIxOOsDFB",
},
});
const provider = new WebTracerProvider({
 resource: new Resource({

   [SemanticResourceAttributes.SERVICE_NAME]: 'frontend-react-js',
 }),
});
provider.addSpanProcessor(new BatchSpanProcessor(exporter));
provider.register({
 contextManager: new ZoneContextManager()
});

registerInstrumentations({
 instrumentations: [
   getWebAutoInstrumentations({
     // load custom configuration for xml-http-request instrumentation
     '@opentelemetry/instrumentation-xml-http-request': {
       propagateTraceHeaderCorsUrls: [
           /api.+/g,
         ],
     },
     // load custom configuration for fetch instrumentation
     '@opentelemetry/instrumentation-fetch': {
       propagateTraceHeaderCorsUrls: [
           /api.+/g,
         ],
     },
   }),
   new DocumentLoadInstrumentation(),
   new UserInteractionInstrumentation(),
   new LongTaskInstrumentation({
    observerCallback: (span, longtaskEvent) => {
      span.setAttribute('location.pathname', window.location.pathname)
    }
  }),
 ],
});