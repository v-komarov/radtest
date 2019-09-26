#!/bin/sh

docker run --rm -d -p 8080:8080 --name radtest \
-e RADIUS_HOST=127.0.0.1 \
-e RADIUS_SECRET=secret \
radtest:first
