import React, { useState } from 'react';
import { Columns, Eye, Sparkles, AlertCircle } from 'lucide-react';

export default function ImageWorkspace({
  originalImage,
  processedImage,
  isProcessing,
  error
}) {
  const [viewMode, setViewMode] = useState('side-by-side'); // 'side-by-side' | 'processed-only' | 'original-only'

  if (!originalImage) {
    return (
      <main className="flex-1 bg-slate-950 flex flex-col items-center justify-center p-8 text-center">
        <div className="w-16 h-16 rounded-2xl bg-slate-900 border border-slate-800 flex items-center justify-center mb-4 text-slate-500">
          <Sparkles className="w-8 h-8 text-cyan-400" />
        </div>
        <h3 className="text-base font-semibold text-white mb-1">Chưa có ảnh nào được chọn</h3>
        <p className="text-xs text-slate-400 max-w-sm mb-4">
          Hãy tải lên một bức ảnh từ máy của bạn hoặc nhấn nút "Ảnh mẫu 1" / "Ảnh mẫu 2" trên thanh công cụ để thử nghiệm.
        </p>
      </main>
    );
  }

  return (
    <main className="flex-1 bg-slate-950 flex flex-col overflow-hidden">
      {/* Workspace Subheader / View Mode Switcher */}
      <div className="h-12 border-b border-slate-800/80 px-6 flex items-center justify-between bg-slate-900/30">
        <div className="flex items-center gap-1 bg-slate-900 p-1 rounded-lg border border-slate-800 text-xs">
          <button
            onClick={() => setViewMode('side-by-side')}
            className={`px-3 py-1 rounded-md transition font-medium flex items-center gap-1.5 ${
              viewMode === 'side-by-side'
                ? 'bg-slate-800 text-cyan-400 shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <Columns className="w-3.5 h-3.5" />
            <span>So sánh song song</span>
          </button>
          <button
            onClick={() => setViewMode('processed-only')}
            className={`px-3 py-1 rounded-md transition font-medium flex items-center gap-1.5 ${
              viewMode === 'processed-only'
                ? 'bg-slate-800 text-cyan-400 shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <Eye className="w-3.5 h-3.5" />
            <span>Chỉ xem kết quả</span>
          </button>
          <button
            onClick={() => setViewMode('original-only')}
            className={`px-3 py-1 rounded-md transition font-medium flex items-center gap-1.5 ${
              viewMode === 'original-only'
                ? 'bg-slate-800 text-cyan-400 shadow-sm'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            <span>Ảnh gốc</span>
          </button>
        </div>

        {error && (
          <div className="flex items-center gap-1.5 text-xs text-rose-400 bg-rose-950/40 px-3 py-1 rounded-md border border-rose-800/50">
            <AlertCircle className="w-3.5 h-3.5" />
            <span>{error}</span>
          </div>
        )}
      </div>

      {/* Canvas Area */}
      <div className="flex-1 overflow-auto p-6 flex items-center justify-center">
        {viewMode === 'side-by-side' && (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 w-full max-w-6xl h-full items-center">
            {/* Original Card */}
            <div className="flex flex-col h-full max-h-[75vh] bg-slate-900/50 rounded-2xl border border-slate-800/80 overflow-hidden shadow-xl">
              <div className="px-4 py-2.5 border-b border-slate-800/80 bg-slate-900/80 flex items-center justify-between text-xs font-semibold text-slate-300">
                <span>Ảnh gốc (Original Input)</span>
                <span className="text-[10px] text-slate-500 font-mono">RGB</span>
              </div>
              <div className="flex-1 bg-slate-950 flex items-center justify-center p-4 overflow-hidden relative">
                <img
                  src={originalImage}
                  alt="Original"
                  className="max-h-full max-w-full object-contain rounded-lg shadow-md"
                />
              </div>
            </div>

            {/* Processed Card */}
            <div className="flex flex-col h-full max-h-[75vh] bg-slate-900/50 rounded-2xl border border-cyan-500/20 overflow-hidden shadow-xl shadow-cyan-950/20">
              <div className="px-4 py-2.5 border-b border-slate-800/80 bg-slate-900/80 flex items-center justify-between text-xs font-semibold text-cyan-400">
                <div className="flex items-center gap-2">
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Kết quả xử lý (OpenCV Output)</span>
                </div>
                {isProcessing && (
                  <span className="text-[10px] font-mono text-cyan-400 animate-pulse">Running...</span>
                )}
              </div>
              <div className="flex-1 bg-slate-950 flex items-center justify-center p-4 overflow-hidden relative">
                {processedImage ? (
                  <img
                    src={`data:image/png;base64,${processedImage}`}
                    alt="Processed"
                    className="max-h-full max-w-full object-contain rounded-lg shadow-md"
                  />
                ) : (
                  <div className="text-xs text-slate-500 animate-pulse">
                    Đang tính toán kết quả...
                  </div>
                )}
              </div>
            </div>
          </div>
        )}

        {viewMode === 'processed-only' && (
          <div className="w-full max-w-4xl h-full max-h-[80vh] flex flex-col bg-slate-900/50 rounded-2xl border border-slate-800 overflow-hidden shadow-2xl">
            <div className="flex-1 bg-slate-950 flex items-center justify-center p-4">
              {processedImage ? (
                <img
                  src={`data:image/png;base64,${processedImage}`}
                  alt="Processed"
                  className="max-h-full max-w-full object-contain rounded-lg"
                />
              ) : (
                <div className="text-xs text-slate-500">Chưa có kết quả xử lý</div>
              )}
            </div>
          </div>
        )}

        {viewMode === 'original-only' && (
          <div className="w-full max-w-4xl h-full max-h-[80vh] flex flex-col bg-slate-900/50 rounded-2xl border border-slate-800 overflow-hidden shadow-2xl">
            <div className="flex-1 bg-slate-950 flex items-center justify-center p-4">
              <img
                src={originalImage}
                alt="Original"
                className="max-h-full max-w-full object-contain rounded-lg"
              />
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
