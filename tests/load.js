import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 1,
  iterations: 5,
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p(95)<2000"],
  },
};

const BASE_URL = __ENV.BASE_URL || "http://localhost:8000";

export default function () {
  const response = http.get(`${BASE_URL}/`);
  check(response, {
    "API responde HTTP 200": (r) => r.status === 200,
    "respuesta contiene version": (r) => {
      try { return Boolean(JSON.parse(r.body).version); }
      catch (_) { return false; }
    },
  });
  sleep(1);
}
