# Resilient-functions

This repository consists of some functions for IBM Resilient.

### fn_check_hsts
This is a simple function for checking whether a response header of a website includes HSTS. 
The input 'domain_name' should be the website domain name you want to check whether HSTS is enabled.
It will return True if HSTS and SSL are enabled and False otherwise.

### fn_enable_hsts
This function can enable/disable HSTS of a Kubernetes Ingress service.
Note that by default, both HSTS and SSL-redirect of nginx ingress controller are enabled. 
To demo the function of HSTS, we disable them in advanced, and use this function to control the kubernetes configmap of nginx ingress controller

### fn_find_collection
This function includes a folder, xfe, which contains all collections existed and accessable from IBM XForceExchange from a user-provided API key. 
A python script is provided in the function to update collections.
The function itself iterates all the collections and return all collections with indicators match to user-provided artifact value

### fn_stix_bundle
This function creates a STIX bundle from artifacts. It includes a csv file with mapping of Resilient-artifact to stix-component.
It use this file to create a STIX bundle and return it.
