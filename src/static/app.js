const AppTitle = <h1>Internet of Tomatos!</h1>;

class Monitor extends React.Component {
  render() {
    return (
      <div>
        <h3>Monitor {this.props.id}</h3>
        <a href={`./api/monitors/${this.props.id}`}>Ver lecturas</a>
      </div>
    );
  }
}

class Monitors extends React.Component {
  render() {
    return (
      <section>
        <p>Below you'll find a list of active monitors.</p>
        <ul>
          <li><Monitor id='01'/></li>
          <li><Monitor id='02'/></li>
          <li><Monitor id='03'/></li>
        </ul>
      </section>
    );
  }
}

class App extends React.Component {
  render() {
    return (
      <main>
        {AppTitle}
        <Monitors />
      </main>
    );
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);