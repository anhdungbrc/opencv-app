import React, { useRef } from 'react';
import { Camera, Upload, Download, Sparkles, RefreshCw, CheckCircle2, AlertCircle } from 'lucide-react';
import { createShapesSample, createNoisySample } from '../utils/sampleImages';

export default function Navbar({
  serverStatus,
  onImageSelected,
  onDownloadResult,
  hasResult,
  isProcessing
}) {
  const fileInputRef = useRef(null);

  const handleFileUpload = (e) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        onImageSelected(event.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <header className="h-16 border-b border-slate-800 bg-slate-900/90 backdrop-blur px-6 flex items-center justify-between sticky top-0 z-50">
      {/* Brand title */}
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/20">
          <Camera className="w-5 h-5 text-white" />
        </div>
        <div>
          <div className="flex items-center gap-2">
            <h1 className="font-bold text-lg text-white tracking-tight">OpenCV Studio</h1>
            <span className="text-[10px] uppercase font-semibold px-2 py-0.5 rounded-full bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
              v1.0
            </span>
          </div>
          <p className="text-xs text-slate-400 hidden sm:block">Interactive Image Processing & Computer Vision</p>
        </div>
      </div>

      {/* Center: Server connection status pill */}
      <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-slate-800/80 border border-slate-700/60 text-xs">
        {serverStatus ? (
          <>
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-slate-300 font-medium hidden md:inline">FastAPI Backend:</span>
            <span className="text-emerald-400 font-mono">Online</span>
          </>
        ) : (
          <>
            <span className="w-2 h-2 rounded-full bg-rose-500" />
            <span className="text-rose-400 font-medium">Backend Offline</span>
          </>
        )}
      </div>

      {/* Right: Quick actions */}
      <div className="flex items-center gap-2.5">
        {/* Sample switcher dropdown */}
        <div className="flex items-center gap-1.5 bg-slate-800/60 p-1 rounded-lg border border-slate-700/50">
          <button
            onClick={() => onImageSelected(createShapesSample())}
            className="px-2.5 py-1 text-xs rounded-md text-slate-300 hover:text-white hover:bg-slate-700/60 transition"
            title="Nạp ảnh mẫu hình học"
          >
            Ảnh mẫu 1
          </button>
          <button
            onClick={() => onImageSelected(createNoisySample())}
            className="px-2.5 py-1 text-xs rounded-md text-slate-300 hover:text-white hover:bg-slate-700/60 transition"
            title="Nạp ảnh mẫu nhiễu"
          >
            Ảnh mẫu 2
          </button>
        </div>

        {/* Upload Button */}
        <input
          type="file"
          ref={fileInputRef}
          onChange={handleFileUpload}
          accept="image/*"
          className="hidden"
        />
        <button
          onClick={() => fileInputRef.current?.click()}
          className="flex items-center gap-2 px-3.5 py-2 text-xs font-semibold rounded-lg bg-blue-600 hover:bg-blue-500 text-white shadow-md shadow-blue-600/20 transition active:scale-95"
        >
          <Upload className="w-3.5 h-3.5" />
          <span>Tải ảnh lên</span>
        </button>

        {/* Download Result Button */}
        <button
          onClick={onDownloadResult}
          disabled={!hasResult}
          className="flex items-center gap-2 px-3 py-2 text-xs font-medium rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/60 disabled:opacity-40 disabled:cursor-not-allowed transition"
          title="Tải ảnh sau xử lý về máy"
        >
          <Download className="w-3.5 h-3.5" />
          <span className="hidden sm:inline">Lưu kết quả</span>
        </button>
      </div>
    </header>
  );
}
