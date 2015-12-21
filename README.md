# simple-docker-app
Simple app to debug openshift


Create the openshift app

```
oc new-app https://github.com/gaelL/simple-docker-app --strategy=docker
oc expose service/simple-docker-app --hostname="simple-docker-app.com"
```

Add the custom domain in your hosts

```
echo 'X.X.X.X simple-docker-app.com' >> /etc/hosts
```

Curl example :

```
curl simple-docker-app.com -vvv

# Get cookie from app
curl --cookie-jar ./cookie.txt simple-docker-app.com -vvv

# With header
curl -H 'myheader: foo' simple-docker-app.com -vvv

# With string cookie
curl --cookie 'mycookie=foo' simple-docker-app.com -vvv
```
