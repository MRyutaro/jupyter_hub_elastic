import {
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import connectionLostPlugin from './connectionLost';

const plugins: JupyterFrontEndPlugin<any>[] = [
  connectionLostPlugin
];

export default plugins;
