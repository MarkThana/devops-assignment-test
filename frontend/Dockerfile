FROM nginx:1.25-alpine

# ลบ default config
RUN rm /etc/nginx/conf.d/default.conf

# copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# copy static html
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80

HEALTHCHECK CMD wget -qO- http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]