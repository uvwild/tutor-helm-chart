# helm chart for an automated  tutor installation on k8s

This fork became necessary due to the number of changes mainly in the helm API.
We cant expect things to work 2 years laster with this kind of technology. <BR>
luckily `helm lint .` is all we need to verify.

using helm 3.4.1  & k8s 1.18.6 & kubectl 1.19.2

installed using 
k create namespace helmtutor
helm --debug install --namespace helmtutor  --generate-name .

## changes
1. requirements.yaml is a requirement now ;)
1. some small template patches
1. version updates of the participating service images
1. deprecation of ingress api
1. missing required field "serviceName" in io.k8s.api.apps.v1.StatefulSetSpec
1. Importing 'lms.djangoapps.courseware' as 'courseware' is no longer supported forces overhang images

## todo
1. configure DJANGO_SETTINGS_MODULE to avoid import of debug_