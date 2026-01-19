import { Component } from "react";
import type { ErrorInfo, ReactNode } from "react";

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null,
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error("Uncaught error:", error, errorInfo);
  }

  public render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen flex items-center justify-center bg-red-50 p-8 text-neutral-900">
          <div className="max-w-2xl w-full bg-white p-8 rounded-2xl shadow-xl border border-red-100">
            <h1 className="text-2xl font-bold text-red-600 mb-4">Application Crashed</h1>
            <p className="mb-4 text-neutral-600">Something went wrong while rendering the application.</p>
            <div className="bg-neutral-900 text-red-300 p-4 rounded-lg font-mono text-sm overflow-auto mb-6">
              {this.state.error?.message}
            </div>
            <button 
                onClick={() => window.location.reload()}
                className="px-6 py-2 bg-neutral-900 text-white rounded-lg hover:bg-neutral-800 transition-colors"
            >
                Reload Page
            </button>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
