import {
  ConnectionLost,
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
  JupyterLab
} from '@jupyterlab/application';
import { IConnectionLost } from '@jupyterlab/application';
// import { showDialog, Dialog } from '@jupyterlab/apputils';
import { ServiceManager, ServerConnection } from '@jupyterlab/services';
import { ITranslator } from '@jupyterlab/translation';


export namespace CommandIDs {
  export const controlPanel: string = 'hub:control-panel';

  export const logout: string = 'hub:logout';

  export const restart: string = 'hub:restart';
}

const connectionLostPlugin: JupyterFrontEndPlugin<IConnectionLost> = {
  id: 'elastic-extension:connection-lost',
  description:
    'Custom connection lost handler for JupyterLab.',
  requires: [JupyterFrontEnd.IPaths, ITranslator],
  optional: [JupyterLab.IInfo],
  activate: (
    app: JupyterFrontEnd,
    paths: JupyterFrontEnd.IPaths,
    translator: ITranslator,
    info: JupyterLab.IInfo | null
  ): IConnectionLost => {
    console.log('JupyterLab Connection Lost Extension is activated!');

    // const trans = translator.load('jupyterlab');
    const hubPrefix = paths.urls.hubPrefix || '';
    // const baseUrl = paths.urls.base;

    // Return the default error message if not running on JupyterHub.
    if (!hubPrefix) {
      return ConnectionLost;
    }

    // If we are running on JupyterHub, return a dialog
    // that prompts the user to restart their server.
    let showingError = false;
    const onConnectionLost: IConnectionLost = async (
      manager: ServiceManager.IManager,
      err: ServerConnection.NetworkError
    ): Promise<void> => {
      if (showingError) {
        return;
      }

      showingError = true;
      if (info) {
        info.isConnected = false;
      }

      // T秒後にリロード
      const T = 5;
      setTimeout(() => {
        location.reload();
        console.log('Reloaded');
      }, T * 1000);

      if (info) {
        info.isConnected = true;
      }
      showingError = false;

    };
    return onConnectionLost;
  },
  autoStart: true,
  provides: IConnectionLost
};

export default connectionLostPlugin;
