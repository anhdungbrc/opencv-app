import React from 'react';
import { Sliders, RotateCcw, ExternalLink, Info, Activity } from 'lucide-react';

export default function ControlPanel({
  operation,
  params,
  onChangeParam,
  onResetParams,
  metadata,
  isProcessing
}) {
  if (!operation) {
    return (
      <div className="w-84 border-l border-slate-800 bg-slate-900/60 p-6 flex items-center justify-center text-xs text-slate-500">
        Chọn một thuật toán từ Sidebar để chỉnh tham số
      </div>
    );
  }

  const parameterList = operation.parameters || [];

  return (
    <div className="w-88 border-l border-slate-800 bg-slate-900/60 flex flex-col h-[calc(100vh-4rem)]">
      {/* Operation Header */}
      <div className="p-4 border-b border-slate-800/80 space-y-2">
        <div className="flex items-center justify-between">
          <span className="text-[10px] font-semibold tracking-wider text-cyan-400 uppercase bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/20">
            {operation.category}
          </span>
          {operation.doc_url && (
            <a
              href={operation.doc_url}
              target="_blank"
              rel="noreferrer"
              className="text-[11px] text-slate-400 hover:text-cyan-400 flex items-center gap-1 transition font-mono"
            >
              <span>Tutorial</span>
              <ExternalLink className="w-3 h-3" />
            </a>
          )}
        </div>
        <h2 className="text-base font-bold text-white tracking-tight">{operation.name}</h2>
        <p className="text-xs text-slate-400 leading-relaxed">{operation.description}</p>
      </div>

      {/* Dynamic Controls List */}
      <div className="flex-1 overflow-y-auto p-4 space-y-5 custom-scrollbar">
        <div className="flex items-center justify-between text-xs font-semibold text-slate-300">
          <div className="flex items-center gap-2">
            <Sliders className="w-3.5 h-3.5 text-cyan-400" />
            <span>Tham số điều khiển</span>
          </div>
          {parameterList.length > 0 && (
            <button
              onClick={onResetParams}
              className="flex items-center gap-1 text-[11px] text-slate-400 hover:text-white transition"
              title="Đặt lại tham số mặc định"
            >
              <RotateCcw className="w-3 h-3" />
              <span>Mặc định</span>
            </button>
          )}
        </div>

        {parameterList.length === 0 ? (
          <div className="p-4 rounded-lg bg-slate-800/40 border border-slate-700/40 text-xs text-slate-400 text-center">
            Thuật toán này chạy trực tiếp không yêu cầu tham số tùy chỉnh.
          </div>
        ) : (
          <div className="space-y-4">
            {parameterList.map((param) => {
              const value = params[param.name] ?? param.default;

              if (param.type === 'slider') {
                return (
                  <div key={param.name} className="space-y-1.5 bg-slate-950/40 p-3 rounded-lg border border-slate-800">
                    <div className="flex items-center justify-between text-xs">
                      <label className="text-slate-300 font-medium">{param.label}</label>
                      <span className="font-mono text-[11px] font-bold text-cyan-400 bg-cyan-950/60 px-2 py-0.5 rounded border border-cyan-800/60">
                        {value}
                      </span>
                    </div>
                    <input
                      type="range"
                      min={param.min}
                      max={param.max}
                      step={param.step || 1}
                      value={value}
                      onChange={(e) => onChangeParam(param.name, Number(e.target.value))}
                      className="w-full accent-cyan-400 h-1.5 bg-slate-800 rounded-lg cursor-pointer"
                    />
                    <div className="flex justify-between text-[10px] text-slate-500 font-mono">
                      <span>{param.min}</span>
                      <span>{param.max}</span>
                    </div>
                  </div>
                );
              }

              if (param.type === 'select') {
                return (
                  <div key={param.name} className="space-y-1.5 bg-slate-950/40 p-3 rounded-lg border border-slate-800">
                    <label className="text-xs font-medium text-slate-300">{param.label}</label>
                    <select
                      value={value}
                      onChange={(e) => onChangeParam(param.name, e.target.value)}
                      className="w-full bg-slate-900 border border-slate-700 rounded-md px-2.5 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-cyan-500"
                    >
                      {param.options?.map((opt) => (
                        <option key={opt} value={opt}>
                          {opt}
                        </option>
                      ))}
                    </select>
                  </div>
                );
              }

              if (param.type === 'checkbox') {
                return (
                  <div
                    key={param.name}
                    className="flex items-center justify-between bg-slate-950/40 p-3 rounded-lg border border-slate-800"
                  >
                    <span className="text-xs font-medium text-slate-300">{param.label}</span>
                    <input
                      type="checkbox"
                      checked={Boolean(value)}
                      onChange={(e) => onChangeParam(param.name, e.target.checked)}
                      className="w-4 h-4 accent-cyan-400 rounded cursor-pointer"
                    />
                  </div>
                );
              }

              return null;
            })}
          </div>
        )}

        {/* Live Processing Indicator */}
        {isProcessing && (
          <div className="flex items-center gap-2 text-xs text-cyan-400 bg-cyan-950/40 px-3 py-2 rounded-lg border border-cyan-800/40">
            <span className="w-2 h-2 rounded-full bg-cyan-400 animate-ping" />
            <span>Đang xử lý qua OpenCV...</span>
          </div>
        )}

        {/* Output Metadata Panel */}
        {metadata && Object.keys(metadata).length > 0 && (
          <div className="mt-4 pt-4 border-t border-slate-800 space-y-2">
            <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-300">
              <Activity className="w-3.5 h-3.5 text-emerald-400" />
              <span>Chỉ số đo đạc (Metadata)</span>
            </div>
            <div className="bg-slate-950 p-3 rounded-lg border border-slate-800 space-y-1.5 font-mono text-[11px]">
              {Object.entries(metadata).map(([k, v]) => (
                <div key={k} className="flex items-center justify-between text-slate-400">
                  <span className="text-slate-500 truncate mr-2">{k}:</span>
                  <span className="text-emerald-400 font-semibold">{String(v)}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
