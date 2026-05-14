export default function CreatorHubStarter() {
  return (
    <div className="min-h-screen bg-black text-white">
      {/* Navbar */}
      <header className="border-b border-white/10 backdrop-blur sticky top-0 z-50 bg-black/70">
        <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white text-black flex items-center justify-center font-bold text-lg">
              C
            </div>
            <div>
              <h1 className="font-bold text-xl">CreatorHub</h1>
              <p className="text-xs text-white/50">Creators x Freelancers</p>
            </div>
          </div>

          <nav className="hidden md:flex gap-8 text-sm text-white/70">
            <a href="#features" className="hover:text-white transition">Features</a>
            <a href="#jobs" className="hover:text-white transition">Jobs</a>
            <a href="#community" className="hover:text-white transition">Community</a>
          </nav>

          <div className="flex gap-3">
            <button className="px-4 py-2 rounded-xl border border-white/15 hover:bg-white/10 transition">
              Login
            </button>
            <button className="px-4 py-2 rounded-xl bg-white text-black font-semibold hover:scale-105 transition">
              Get Started
            </button>
          </div>
        </div>
      </header>

      {/* Hero */}
      <section className="max-w-7xl mx-auto px-6 py-24 grid lg:grid-cols-2 gap-14 items-center">
        <div>
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-white/10 bg-white/5 text-sm text-white/70 mb-6">
            🚀 New generation creator marketplace
          </div>

          <h1 className="text-5xl md:text-7xl font-black leading-tight">
            Find creators.
            <br />
            Build teams.
            <br />
            Grow faster.
          </h1>

          <p className="text-lg text-white/60 mt-8 max-w-xl leading-relaxed">
            A modern platform where creators, editors, thumbnail artists,
            Minecraft builders and freelancers connect instantly.
          </p>

          <div className="flex flex-wrap gap-4 mt-10">
            <button className="px-7 py-4 rounded-2xl bg-white text-black font-bold hover:scale-105 transition">
              Start Hiring
            </button>

            <button className="px-7 py-4 rounded-2xl border border-white/15 hover:bg-white/10 transition">
              Explore Jobs
            </button>
          </div>

          <div className="flex gap-10 mt-14">
            <div>
              <h2 className="text-3xl font-bold">12K+</h2>
              <p className="text-white/50">Creators</p>
            </div>

            <div>
              <h2 className="text-3xl font-bold">48K+</h2>
              <p className="text-white/50">Projects</p>
            </div>

            <div>
              <h2 className="text-3xl font-bold">95%</h2>
              <p className="text-white/50">Positive Reviews</p>
            </div>
          </div>
        </div>

        {/* Right Card */}
        <div className="relative">
          <div className="absolute inset-0 bg-white/10 blur-3xl rounded-full" />

          <div className="relative bg-white/5 border border-white/10 rounded-3xl p-6 backdrop-blur-xl shadow-2xl">
            <div className="flex items-center justify-between mb-6">
              <div>
                <p className="text-white/50 text-sm">Trending Job</p>
                <h3 className="text-2xl font-bold mt-1">
                  Minecraft Builder Needed
                </h3>
              </div>

              <div className="px-4 py-2 rounded-xl bg-green-500/20 text-green-300 text-sm border border-green-500/20">
                OPEN
              </div>
            </div>

            <div className="space-y-4 text-white/70">
              <div className="flex justify-between border-b border-white/10 pb-3">
                <span>Budget</span>
                <span className="font-semibold text-white">$120</span>
              </div>

              <div className="flex justify-between border-b border-white/10 pb-3">
                <span>Category</span>
                <span className="font-semibold text-white">Building</span>
              </div>

              <div className="flex justify-between border-b border-white/10 pb-3">
                <span>Applications</span>
                <span className="font-semibold text-white">24</span>
              </div>
            </div>

            <button className="w-full mt-8 py-4 rounded-2xl bg-white text-black font-bold hover:scale-[1.02] transition">
              Apply Now
            </button>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="max-w-7xl mx-auto px-6 py-20">
        <div className="text-center mb-16">
          <h2 className="text-4xl font-black">Everything creators need</h2>
          <p className="text-white/60 mt-4 text-lg">
            Fast, modern and built for internet culture.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          {[
            {
              title: 'Post Jobs',
              desc: 'Find editors, designers, builders and more instantly.',
            },
            {
              title: 'Creator Profiles',
              desc: 'Build reputation with reviews and portfolios.',
            },
            {
              title: 'Fast Communication',
              desc: 'Connect quickly with modern messaging tools.',
            },
          ].map((item, index) => (
            <div
              key={index}
              className="bg-white/5 border border-white/10 rounded-3xl p-8 hover:bg-white/10 transition"
            >
              <div className="w-14 h-14 rounded-2xl bg-white text-black flex items-center justify-center text-2xl font-black mb-6">
                {index + 1}
              </div>

              <h3 className="text-2xl font-bold mb-3">{item.title}</h3>
              <p className="text-white/60 leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-white/10 mt-20">
        <div className="max-w-7xl mx-auto px-6 py-10 flex flex-col md:flex-row justify-between items-center gap-4 text-white/50 text-sm">
          <p>© 2026 CreatorHub. Built for creators.</p>

          <div className="flex gap-6">
            <a href="#" className="hover:text-white transition">Twitter</a>
            <a href="#" className="hover:text-white transition">Discord</a>
            <a href="#" className="hover:text-white transition">GitHub</a>
          </div>
        </div>
      </footer>
    </div>
  )
}

