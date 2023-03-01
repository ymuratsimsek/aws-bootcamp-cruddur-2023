FROM node:16.18 as builder

WORKDIR /frontend-react-js
COPY package*.json ./
RUN npm install
ARG REACT_APP_BACKEND_URL
ENV REACT_APP_BACKEND_URL $REACT_APP_BACKEND_URL
COPY . ./
RUN npm run build
# ========= RUN =========
FROM nginx:1.17
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /frontend-react-js/build .
COPY nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT ["nginx", "-g", "daemon off;"]
