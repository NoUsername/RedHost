# RedHost

Tiny hostname based http redirector service.

You have a small local network and frequently need to access certain services within that network.
Of course you already have a local DNS server, however many of your little services don't run on port 80, you are too lazy to set up a proper proxy and you want to be able to access them via multiple names anyway.

RedHost to the rescue!

## Example

```
# setup
pip install -r requirements.txt

# configure (see below)
nano red.yaml

# run
sudo python redhost.py
```

Example configuration which does several redirects:

```
portRedirects:
  "photo.svc" : "8080"
  "music.svc" : "8081"
  "video.svc" : "8082"


redirects:
  "storage.lan" : "http://192.168.1.10:8080"
```

Such a configuration is particularly useful if you set up your dns server to proxy all `*.svc` requests to the host which runs RedHost. In this case the host running RedHost also runs a lot of other services, therefore we only need the `portRedirects` which will only change the requested port and leave the hostname as is.

If you then request `http://photo.svc/` in your browser you would be redirected to `http://photo.svc:8080/`. 

If you want "full" redirects simply put it in the `redirects` section.

### Example dnsmasq config

To get the `*.svc` redirect as described above add this line to your dnsmasq config:

```
address=/.svc/192.168.1.2
```

This would resolve any `.svc` addresses you request always to the 192.168.1.2 address.

(c) 2016 Paul Klingelhuber
