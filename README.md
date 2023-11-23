# Rio Aero Club website

rioaeroclub.com


## Production

On production, you probably want in `.env`:

```
USER_RUN=1001
GROUP_RUN=1001
PORT=9001

DJANGO_SETTINGS_MODULE=rioaeroclub.settings
DJANGO_SECRET_KEY=''
```

```
systemctl stop docker-compose@rioaeroclub
systemctl start docker-compose@rioaeroclub
```