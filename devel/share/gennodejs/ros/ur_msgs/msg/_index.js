
"use strict";

let Analog = require('./Analog.js');
let Digital = require('./Digital.js');
let MasterboardDataMsg = require('./MasterboardDataMsg.js');
let RobotModeDataMsg = require('./RobotModeDataMsg.js');
let ToolDataMsg = require('./ToolDataMsg.js');
let IOStates = require('./IOStates.js');
let RobotStateRTMsg = require('./RobotStateRTMsg.js');

module.exports = {
  Analog: Analog,
  Digital: Digital,
  MasterboardDataMsg: MasterboardDataMsg,
  RobotModeDataMsg: RobotModeDataMsg,
  ToolDataMsg: ToolDataMsg,
  IOStates: IOStates,
  RobotStateRTMsg: RobotStateRTMsg,
};
