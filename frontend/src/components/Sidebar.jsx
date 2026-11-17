import React, { useState } from 'react';
import {
  Palette,
  Sliders,
  Droplet,
  Zap,
  Repeat,
  CircleDot,
  BarChart2,
  Move,
  Search,
  BookOpen,
  ChevronRight
} from 'lucide-react';

const CATEGORY_ICONS = {
  'Colorspaces': Palette,
  'Thresholding': Sliders,
  'Smoothing': Droplet,
  'Edges & Gradients': Zap,
  'Morphology': Repeat,
  'Contours': CircleDot,
  'Histograms': BarChart2,
  'Geometric': Move,
};

export default function Sidebar({ operations, selectedOpId, onSelectOperation }) {
  const [searchQuery, setSearchQuery] = useState('');

  // Group operations by category
  const grouped = operations.reduce((acc, op) => {
    const cat = op.category || 'General';
    if (!acc[cat]) acc[cat] = [];
    acc[cat].push(op);
    return acc;
  }, {});

  const filteredCategories = Object.entries(grouped).map(([category, ops]) => {
    const matchingOps = ops.filter(
      (op) =>
        op.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        op.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
        op.id.toLowerCase().includes(searchQuery.toLowerCase())
    );
    return { category, ops: matchingOps };
  }).filter((group) => group.ops.length > 0);

  return (
    <aside className="w-80 border-r border-slate-800 bg-slate-900/60 flex flex-col h-[calc(100vh-4rem)]">
      {/* Search Input */}
      <div className="p-4 border-b border-slate-800/80">
        <div className="relative">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Tìm thuật toán OpenCV..."
            className="w-full bg-slate-950/80 border border-slate-700/80 rounded-lg pl-9 pr-3 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-cyan-500/80 transition"
          />
        </div>
      </div>

      {/* Operations List */}
      <div className="flex-1 overflow-y-auto p-3 space-y-4 custom-scrollbar">
        {filteredCategories.map(({ category, ops }) => {
          const Icon = CATEGORY_ICONS[category] || BookOpen;
          return (
            <div key={category} className="space-y-1">
              {/* Category Header */}
              <div className="flex items-center gap-2 px-2.5 py-1 text-[11px] font-semibold tracking-wider text-slate-400 uppercase">
                <Icon className="w-3.5 h-3.5 text-cyan-400" />
                <span>{category}</span>
                <span className="text-slate-600 font-mono text-[10px]">({ops.length})</span>
              </div>

              {/* Items */}
              <div className="space-y-0.5">
                {ops.map((op) => {
                  const isSelected = op.id === selectedOpId;
                  return (
                    <button
                      key={op.id}
                      onClick={() => onSelectOperation(op.id)}
                      className={`w-full text-left px-3 py-2 rounded-lg text-xs transition flex items-center justify-between group ${
                        isSelected
                          ? 'bg-cyan-500/10 text-cyan-400 border border-cyan-500/30 font-medium shadow-sm'
                          : 'text-slate-300 hover:bg-slate-800/50 hover:text-white'
                      }`}
                    >
                      <div className="truncate pr-2">
                        <div className="truncate">{op.name}</div>
                        <div className="text-[10px] text-slate-500 font-mono truncate">{op.id}</div>
                      </div>
                      <ChevronRight
                        className={`w-3.5 h-3.5 transition-transform shrink-0 ${
                          isSelected ? 'text-cyan-400 translate-x-0.5' : 'text-slate-600 group-hover:text-slate-400'
                        }`}
                      />
                    </button>
                  );
                })}
              </div>
            </div>
          );
        })}

        {filteredCategories.length === 0 && (
          <div className="p-6 text-center text-xs text-slate-500">
            Không tìm thấy thuật toán nào khớp với "{searchQuery}"
          </div>
        )}
      </div>

      {/* Footer link to OpenCV tutorial */}
      <div className="p-3 border-t border-slate-800 bg-slate-950/40 text-[11px] text-slate-400 flex items-center justify-between">
        <span>Tài liệu nguồn:</span>
        <a
          href="https://docs.opencv.org/3.4.20/d2/d96/tutorial_py_table_of_contents_imgproc.html"
          target="_blank"
          rel="noreferrer"
          className="text-cyan-400 hover:underline flex items-center gap-1 font-mono"
        >
          OpenCV docs ↗
        </a>
      </div>
    </aside>
  );
}
