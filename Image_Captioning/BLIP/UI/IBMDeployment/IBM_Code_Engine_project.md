
#### IBM Code Engine project
# IBM Code Engine is a fully managed, serverless platform that runs your containerized workloads, including web apps, micro-services, event-driven functions, or batch jobs. Code Engine even builds container images for you from your source code. All these workloads can seamlessly work together because they are all hosted within the same Kubernetes infrastructure. The Code Engine experience is designed so that you can focus on writing code and not on the infrastructure that is needed to host it.

# ibmcloud ce project current
# 
# Name:       Code Engine - sn-labs-manisharadha  
# ID:         aff953ed-1c71-4f1c-84e1-1517ae821b94  
# Subdomain:  206wrjxjrq5f  
# Domain:     us-south.codeengine.appdomain.cloud  
# Region:     us-south  

# Kubernetes Config:    
# Context:               206wrjxjrq5f  
# Environment Variable:  export KUBECONFIG="/home/theia/.bluemix/plugins/code-engine/Code Engine - sn-labs-manisharadha-aff953ed-1c71-4f1c-84e1-1517ae821b94.yaml"  

# ibmcloud ce project get --id aff953ed-1c71-4f1c-84e1-1517ae821b94

# Creating the build configuration
``` shell 
ibmcloud ce build create --name build-local-dockerfile1 \
                        --build-type local --size large \
                        --image us.icr.io/${SN_ICR_NAMESPACE}/myapp1 \
                        --registry-secret icr-secret
                        /
```

# Submitting and running the build configuration
``` shell 
ibmcloud ce buildrun submit --name buildrun-local-dockerfile1 \
                            --build build-local-dockerfile1 \
                            --source .
                            /
```
* To monitor the progress of the buildrun, use the following command:
``` shell 
ibmcloud ce buildrun get -n buildrun-local-dockerfile1
```
# Creating your application
``` shell
ibmcloud ce application create --name demo1 \
                            --image us.icr.io/${SN_ICR_NAMESPACE}/myapp1  \
                            --registry-secret icr-secret --es 2G \
                            --port 7860 --minscale 1
```
# Accessing your application
``` shell
ibmcloud ce app get --name demo1 --output url
```
* url: https://demo1.206wrjxjrq5f.us-south.codeengine.appdomain.cloud