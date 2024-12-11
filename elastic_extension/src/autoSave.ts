import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import {
  INotebookTracker
} from '@jupyterlab/notebook';
import {
  NotebookActions
} from '@jupyterlab/notebook';

const autoSavePlugin: JupyterFrontEndPlugin<void> = {
  id: 'elastic-extension:auto-save',
  description: 'Auto save notebooks after cell execution.',
  autoStart: true,
  requires: [INotebookTracker],
  activate: (app: JupyterFrontEnd, notebookTracker: INotebookTracker) => {
    console.log('JupyterLab Auto Save Extension is activated!');

    let isConnected = false;

    notebookTracker.activeCellChanged.connect((tracker) => {
      const notebookPanel = tracker.currentWidget;
      if (notebookPanel) {
        const sessionContext = notebookPanel.context;

        if (!isConnected) {
          isConnected = true;
          // Hook into the cell execution process
          NotebookActions.executed.connect(() => {
            if (sessionContext && sessionContext.isReady) {
              sessionContext.save();
              console.log('Notebook auto-saved after cell execution.');
            }
          });
        }
      }
    });
  }
};

export default autoSavePlugin;
