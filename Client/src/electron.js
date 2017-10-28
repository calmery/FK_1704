import electron from 'electron'

const app = electron.app

app.on( 'window-all-closed', () => app.quit() )

export default options => {
  options = options || {}

  return new Promise( ( resolve, reject ) => {
    const BrowserWindow = electron.BrowserWindow

    const create = () => {
      options.show = false
      let main = new BrowserWindow( options )

      main.once( 'ready-to-show', () => main.show() )

      resolve( main )
    }

    if( app.isReady() === true )
      create()
    else
      app.on( 'ready', create )
  } )
}
