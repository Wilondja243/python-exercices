import nmap3

nmap = nmap3.NmapScanTechniques()
print(nmap)
result = nmap.nmap_syn_scan()

print(result)