const API_BASE = "";

async function request(path, options = {}) {
  const res = await fetch(path, {
    credentials: "include",
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {})
    },
    ...options
  });

  if (!res.ok) {
    throw new Error("Request failed");
  }

  return res.json();
}

export function getDashboard() {
  return request("/dashboard");
}

export function getWorkflow() {
  return request("/workflow");
}

export function submitAppeal(trace) {
  return request("/appeal", {
    method: "POST",
    body: JSON.stringify(trace)
  });
}
