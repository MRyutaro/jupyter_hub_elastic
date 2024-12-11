import {
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import autoSavePlugin from './autoSave';
import connectionLostPlugin from './connectionLost';

const plugins: JupyterFrontEndPlugin<any>[] = [
  autoSavePlugin,
  connectionLostPlugin,
];

export default plugins;
