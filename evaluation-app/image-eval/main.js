const { app, BrowserWindow } = require("electron");
const path = require("path");
const url = require("url");

let win;
function createWindow() {
  win = new BrowserWindow({ width: 700, height: 700 });
  // load the dist folder from Angular
  win.loadURL(
    url.format({

      // compiled version of our app
      pathname: path.join(__dirname, '/dist/index.html'),
      protocol: "file:",
      slashes: true
    })
  );
  win.on("closed", () => {
    win = null;
  });
}
app.on("ready", createWindow);
// If you are using MACOS, we have to quit the app manually 
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

// const { app, BrowserWindow } = require('electron')
//
// let win;
//
// function createWindow () {
//   // Create the browser window.
//   win = new BrowserWindow({
//     width: 600,
//     height: 600,
//     backgroundColor: '#ffffff',
//     icon: `file://${__dirname}/dist/assets/logo.png`
//   })
//
//
//   win.loadURL(`file://${__dirname}/dist/image-eval/index.html`)
//
//
//
//
//   //// uncomment below to open the DevTools.
//   // win.webContents.openDevTools()
//
//   // Event when the window is closed.
//   win.on('closed', function () {
//     win = null
//   })
// }
//
// // Create window on electron intialization
// app.on('ready', createWindow)
//
// // Quit when all windows are closed.
// app.on('window-all-closed', function () {
//
//   // On macOS specific close process
//   if (process.platform !== 'darwin') {
//     app.quit()
//   }
// })
//
// app.on('activate', function () {
//   // macOS specific close process
//   if (win === null) {
//     createWindow()
//   }
// })
