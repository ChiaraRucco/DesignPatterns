import './style.css'
import javascriptLogo from './javascript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.js'

document.querySelector('#app').innerHTML = `
  <div>
    <a href="https://vite.dev" target="_blank">
      <img src="${viteLogo}" class="logo" alt="Vite logo" />
    </a>
    <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank">
      <img src="${javascriptLogo}" class="logo vanilla" alt="JavaScript logo" />
    </a>
    <h1>Hello Vite!</h1>
    <nav>
      <button id="nav-introduction">Introduction</button>
      <button id="nav-design-patterns">Design Patterns</button>
      <button id="nav-llms">LLMs</button>
    </nav>
    <div id="content"></div>
    <div class="card">
      <button id="counter" type="button"></button>
    </div>
    <p class="read-the-docs">
      Click on the Vite logo to learn more
    </p>
  </div>
`

setupCounter(document.querySelector('#counter'))

const loadContent = (contentId) => {
  const content = {
    introduction: `
      <section id="introduction">
        <h2>Introduction</h2>
        <p>In the contemporary digital ecosystem, data has become a strategic asset and a cornerstone of organizational intelligence. This research introduces a structured framework of Data Engineering Design Patterns for agile and sustainable data management.</p>
      </section>
    `,
    designPatterns: `
      <section id="design-patterns">
        <h2>Core Design Patterns</h2>
        <article>
          <h3>MIND (Metadata-driven INgestion Design Pattern)</h3>
          <p>Addresses challenges in metadata management during data ingestion.</p>
        </article>
        <article>
          <h3>ETLT/ELTL++ (Hybrid Transformation Patterns)</h3>
          <p>Optimizes transformation timing for hybrid data pipelines.</p>
        </article>
        <article>
          <h3>EADF (Environment-Aware Deployment Framework)</h3>
          <p>Ensures deployment consistency across environments.</p>
        </article>
      </section>
    `,
    llms: `
      <section id="llms">
        <h2>Role of Large Language Models</h2>
        <p>Experimental benchmarking of advanced models like GPT-5 and Claude demonstrates their potential in pipeline code generation, validation, and design mediation.</p>
      </section>
    `,
  };

  document.getElementById('content').innerHTML = content[contentId] || '<p>Content not found.</p>';
};

document.getElementById('nav-introduction').addEventListener('click', () => loadContent('introduction'));
document.getElementById('nav-design-patterns').addEventListener('click', () => loadContent('designPatterns'));
document.getElementById('nav-llms').addEventListener('click', () => loadContent('llms'));

// Load the introduction content by default
loadContent('introduction');
