# helm chart for an automated  tutor installation on k8s

This fork became necessary due to the number of changes mainly in the helm API.
We cant expect things to work 2 years laster with this kind of technology. <BR>
luckily `helm lint .` is all we need to verify.

## changes
1. requirements.yaml is a requirement now ;)
1. some small template patches
1. version updates of the participating service images
1. deprecation of ingress api