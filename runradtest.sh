#!/bin/sh

docker run --rm -d -p 8080:8080 --name radtest \
--link freeradius:freeradius \
-e RADIUS_HOST=freeradius \
-e RADIUS_SECRET=secret \
radtest:first
