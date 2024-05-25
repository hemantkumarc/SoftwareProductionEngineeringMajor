const winston = require('winston');
const Elasticsearch = require('winston-elasticsearch');

const esTransportOpts = {
  level: 'info',
  clientOpts: {
    node: 'https://b02d0e7d46454e68a7a14c549d4643db.us-central1.gcp.cloud.es.io:443', // Your ELK endpoint
    auth: {
      apiKey: 'gUj_XKhCRJW9NlpZCgc2qA' // Your API key
    },
    cloud: {
      id: 'CourseMap_ELK_Stack:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGIwMmQwZTdkNDY0NTRlNjhhN2ExNGM1NDlkNDY0M2RiJDFjNjM2ZWQxY2VkMTRjMDNiZWE3NjZlY2QxNWVkOWJl' // Your Cloud ID
    }
  }
};

const logger = winston.createLogger({
  transports: [
    new winston.transports.Console(),
    new Elasticsearch(esTransportOpts)
  ]
});

module.exports = logger;
