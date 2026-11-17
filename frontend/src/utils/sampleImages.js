/**
 * Generates synthetic sample images via HTML5 Canvas for immediate 1-click testing.
 */

export function createShapesSample() {
  const canvas = document.createElement('canvas');
  canvas.width = 640;
  canvas.height = 480;
  const ctx = canvas.getContext('2d');

  // Background
  ctx.fillStyle = '#f8fafc';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Red rectangle
  ctx.fillStyle = '#ef4444';
  ctx.fillRect(60, 60, 160, 120);

  // Blue circle
  ctx.fillStyle = '#3b82f6';
  ctx.beginPath();
  ctx.arc(420, 140, 70, 0, Math.PI * 2);
  ctx.fill();

  // Green triangle
  ctx.fillStyle = '#10b981';
  ctx.beginPath();
  ctx.moveTo(140, 240);
  ctx.lineTo(240, 400);
  ctx.lineTo(40, 400);
  ctx.closePath();
  ctx.fill();

  // Yellow rounded rect
  ctx.fillStyle = '#f59e0b';
  ctx.beginPath();
  ctx.roundRect(320, 280, 240, 120, 20);
  ctx.fill();

  // Fine black technical lines for edge detection
  ctx.strokeStyle = '#0f172a';
  ctx.lineWidth = 3;
  ctx.strokeRect(30, 30, 580, 420);
  ctx.beginPath();
  ctx.moveTo(250, 60);
  ctx.lineTo(250, 420);
  ctx.stroke();

  return canvas.toDataURL('image/png');
}

export function createNoisySample() {
  const canvas = document.createElement('canvas');
  canvas.width = 500;
  canvas.height = 350;
  const ctx = canvas.getContext('2d');

  // Clean base
  ctx.fillStyle = '#e2e8f0';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Big dark circle
  ctx.fillStyle = '#1e293b';
  ctx.beginPath();
  ctx.arc(250, 175, 100, 0, Math.PI * 2);
  ctx.fill();

  // Add synthetic salt & pepper noise
  const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
  const data = imgData.data;
  for (let i = 0; i < data.length; i += 4) {
    const rand = Math.random();
    if (rand < 0.05) {
      // Salt (white)
      data[i] = 255;
      data[i + 1] = 255;
      data[i + 2] = 255;
    } else if (rand > 0.95) {
      // Pepper (black)
      data[i] = 0;
      data[i + 1] = 0;
      data[i + 2] = 0;
    }
  }
  ctx.putImageData(imgData, 0, 0);
  return canvas.toDataURL('image/png');
}
