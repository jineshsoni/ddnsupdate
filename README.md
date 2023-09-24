# ddnsupdate
Use cloudflare as your own ddns service

pre-requisite
Domain must be managed by cloudflare.com (transfer name server)

steps
1. Get recordId of managed domain : [https://developers.cloudflare.com/api/operations/access-identity-providers-list-access-identity-providers](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-dns-record-details)
2. To get all params go through: [https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-dns-record-details](https://developers.cloudflare.com/api/operations/dns-records-for-a-zone-dns-record-details)
3. run the python script, add it in cron to update dns at regular interval
