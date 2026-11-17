/**
 * API service communicating with the FastAPI OpenCV Backend.
 */

const BASE_URL = '/api/v1';

export async function fetchHealth() {
  try {
    const res = await fetch(`${BASE_URL}/health`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error('Backend health check failed:', err);
    return null;
  }
}

export async function fetchOperations() {
  const res = await fetch(`${BASE_URL}/operations`);
  if (!res.ok) {
    throw new Error(`Failed to fetch operations: ${res.statusText}`);
  }
  return await res.json();
}

export async function processImage(imageBase64, operationId, params = {}) {
  const payload = {
    image_base64: imageBase64,
    operation: operationId,
    params: params,
  };

  const res = await fetch(`${BASE_URL}/process`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({}));
    throw new Error(errorData.detail || `Processing error: ${res.statusText}`);
  }

  return await res.json();
}
