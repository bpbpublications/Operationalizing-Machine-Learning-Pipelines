SERVICE_HOSTNAME=$(kubectl get inferenceservice <model_name> -o jsonpath='{.status.url}' | cut -d "/" -f 3)
INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

curl -v \
    -H "Host: ${SERVICE_HOSTNAME}" \
    -H "Content-Type: application/json" \
    -d @./input.json \
    http://${INGRESS_HOST}:${INGRESS_PORT}/v2/models/<model_name>/infer