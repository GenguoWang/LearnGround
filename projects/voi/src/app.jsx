import React from 'react'
import css from './app.css'

class App extends React.PureComponent {
  constructor(props) {
    super(props)
  }
  componentDidMount() {
  }
  componentWillUnmount() {
  }
  render() {
    return <div className={css.app} ref="rootNode">
      Hello World
    </div>
  }
}

export default App
