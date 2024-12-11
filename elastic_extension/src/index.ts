import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

/**
 * Initialization data for the elastic-extension extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'elastic-extension:plugin',
  description: 'A JupyterLab extension.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension elastic-extension is activated!');
  }
};

export default plugin;
