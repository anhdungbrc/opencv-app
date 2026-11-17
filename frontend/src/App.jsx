import React, { useState, useEffect, useCallback, useRef } from 'react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import ControlPanel from './components/ControlPanel';
import ImageWorkspace from './components/ImageWorkspace';
import { fetchHealth, fetchOperations, processImage } from './services/api';
import { createShapesSample } from './utils/sampleImages';

export default function App() {
  const [operations, setOperations] = useState([]);
  const [selectedOpId, setSelectedOpId] = useState('canny_edge');
  const [params, setParams] = useState({});
  const [originalImage, setOriginalImage] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);
  const [metadata, setMetadata] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);
  const [serverStatus, setServerStatus] = useState(false);
  const [error, setError] = useState(null);

  const debounceTimerRef = useRef(null);

  // 1. Initial Load: check backend health and fetch operation list
  useEffect(() => {
    async function init() {
      const health = await fetchHealth();
      setServerStatus(Boolean(health));

      try {
        const ops = await fetchOperations();
        setOperations(ops);
        if (ops.length > 0) {
          // Default to Canny edge or first op
          const defaultOp = ops.find((o) => o.id === 'canny_edge') || ops[0];
          setSelectedOpId(defaultOp.id);
          initParamsForOp(defaultOp);
        }
      } catch (err) {
        console.error('Failed to load operations:', err);
        setError('Không thể kết nối đến Backend FastAPI. Hãy đảm bảo server đang chạy ở port 8000.');
      }

      // Preload initial sample image
      setOriginalImage(createShapesSample());
    }

    init();
  }, []);

  // Helper: initialize default parameter values for an operation
  const initParamsForOp = (op) => {
    const defaults = {};
    op.parameters?.forEach((p) => {
      defaults[p.name] = p.default;
    });
    setParams(defaults);
  };

  // 2. Select operation
  const handleSelectOperation = (opId) => {
    setSelectedOpId(opId);
    const op = operations.find((o) => o.id === opId);
    if (op) {
      initParamsForOp(op);
    }
  };

  // 3. Change parameter with live debounce
  const handleChangeParam = (name, value) => {
    setParams((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  // 4. Reset parameter
  const handleResetParams = () => {
    const op = operations.find((o) => o.id === selectedOpId);
    if (op) {
      initParamsForOp(op);
    }
  };

  // 5. Trigger processing whenever originalImage, selectedOpId, or params change
  const executeProcessing = useCallback(async () => {
    if (!originalImage || !selectedOpId) return;

    setIsProcessing(true);
    setError(null);

    try {
      const response = await processImage(originalImage, selectedOpId, params);
      if (response.success) {
        setProcessedImage(response.result_image_base64);
        setMetadata(response.metadata);
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setIsProcessing(false);
    }
  }, [originalImage, selectedOpId, params]);

  // Debounced auto-run
  useEffect(() => {
    if (debounceTimerRef.current) {
      clearTimeout(debounceTimerRef.current);
    }

    debounceTimerRef.current = setTimeout(() => {
      executeProcessing();
    }, 150); // 150ms debounce for responsive slider feedback

    return () => {
      if (debounceTimerRef.current) {
        clearTimeout(debounceTimerRef.current);
      }
    };
  }, [executeProcessing]);

  // Download result image
  const handleDownloadResult = () => {
    if (!processedImage) return;
    const link = document.createElement('a');
    link.href = `data:image/png;base64,${processedImage}`;
    link.download = `opencv_result_${selectedOpId}.png`;
    link.click();
  };

  const selectedOp = operations.find((o) => o.id === selectedOpId);

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100">
      <Navbar
        serverStatus={serverStatus}
        onImageSelected={setOriginalImage}
        onDownloadResult={handleDownloadResult}
        hasResult={Boolean(processedImage)}
        isProcessing={isProcessing}
      />

      <div className="flex-1 flex overflow-hidden">
        {/* Left: Operations Directory Sidebar */}
        <Sidebar
          operations={operations}
          selectedOpId={selectedOpId}
          onSelectOperation={handleSelectOperation}
        />

        {/* Center: Image Comparison Canvas */}
        <ImageWorkspace
          originalImage={originalImage}
          processedImage={processedImage}
          isProcessing={isProcessing}
          error={error}
        />

        {/* Right: Dynamic Parameters Control Panel */}
        <ControlPanel
          operation={selectedOp}
          params={params}
          onChangeParam={handleChangeParam}
          onResetParams={handleResetParams}
          metadata={metadata}
          isProcessing={isProcessing}
        />
      </div>
    </div>
  );
}
