import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { IConnectionLost } from '@jupyterlab/application';
import { showDialog, Dialog } from '@jupyterlab/apputils';
import { ServiceManager, ServerConnection } from '@jupyterlab/services';

/**
 * Custom implementation of the connection lost handler.
 */
const customConnectionLost: IConnectionLost = async (
  manager: ServiceManager.IManager,
  error: ServerConnection.NetworkError
): Promise<void> => {
  console.warn('Custom connection lost handler invoked.');

  const result = await showDialog({
    title: 'Connection Lost',
    body: 'Custom message: The server connection was lost. Do you want to retry?',
    buttons: [
      Dialog.okButton({ label: 'Retry' }),
      Dialog.cancelButton({ label: 'Dismiss' })
    ]
  });

  if (result.button.accept) {
    // Example of custom retry logic
    console.log('Retrying connection...');
    // Add custom retry logic here, such as reinitializing the manager.
  }
};

const connectionLostPlugin: JupyterFrontEndPlugin<IConnectionLost> = {
  id: 'elastic-extension:connection-lost',
  description: 'Custom connection lost handler for JupyterLab.',
  provides: IConnectionLost,
  autoStart: true,
  activate: (app: JupyterFrontEnd): IConnectionLost => {
    console.log('Custom connection lost plugin activated.');
    return customConnectionLost;
  }
};

export default connectionLostPlugin;
