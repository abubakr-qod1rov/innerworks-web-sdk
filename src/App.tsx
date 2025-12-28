import { useState, useEffect, useRef } from 'react'
import { InnerworksMetrics } from '@innerworks-me/iw-auth-sdk'
import './App.css'

const browsers = [
  'Chrome',
  'Firefox',
  'Safari',
  'Edge',
  'Opera',
  'Brave',
  'Arc',
  'Vivaldi',
  'Samsung Internet'
]

function App() {
  const [email] = useState('abubakr.hbai@gmail.com')
  const [name] = useState('Abubakr')
  const [deviceName, setDeviceName] = useState('')
  const [browserName, setBrowserName] = useState('')
  const [isDropdownOpen, setIsDropdownOpen] = useState(false)
  const [projectId] = useState('e9933f85-5b08-4f08-ad98-4f8213d26eae')
  const [loading, setLoading] = useState(false)
  const [response, setResponse] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)
  const [userId, setUserId] = useState('')
  const dropdownRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (email && name && deviceName && browserName) {
      const constructedUserId = `${email}_${name}_${deviceName}_${browserName}`
      setUserId(constructedUserId)
    }
  }, [email, name, deviceName, browserName])

  const handleSendMetrics = async () => {
    if (!deviceName.trim() || !browserName.trim()) {
      setError('Qurilma nomi va Brauzer nomini to\'ldiring')
      return
    }

    setLoading(true)
    setError(null)
    setSuccess(false)
    setResponse(null)

    try {
      const innerworks = new InnerworksMetrics({
        appId: projectId,
        apiUrl: 'https://api.dev.innerworks.me/api/v1',
        logLevel: 'debug',
        silentLogs: false
      })

      const result = await innerworks.sendMetrics(userId)
      setResponse(result)
      setSuccess(true)

      // Auto-refresh after 3 seconds
      setTimeout(() => {
        window.location.reload()
      }, 3000)
    } catch (err: any) {
      console.error('Error sending metrics:', err)
      setError(err.message || err.toString() || 'Metrikalarni yuborishda xatolik')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    if (userId) {
      handleSendMetrics()
    }
  }, [])

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsDropdownOpen(false)
      }
    }

    document.addEventListener('mousedown', handleClickOutside)
    return () => document.removeEventListener('mousedown', handleClickOutside)
  }, [])

  const handleBrowserSelect = (browser: string) => {
    setBrowserName(browser)
    setIsDropdownOpen(false)
  }

  return (
    <div className="app">
      <div className="container">
        <h1>InnerWorks Web SDK Demosi</h1>
        <p className="subtitle">Qurilma identifikatsiyasi va metrikalar yig'ish</p>

        <div className="card">
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="deviceName">Qurilma nomi</label>
              <input
                id="deviceName"
                type="text"
                value={deviceName}
                onChange={(e) => setDeviceName(e.target.value)}
                placeholder="Masalan: MacbookProIntel"
              />
            </div>

            <div className="form-group">
              <label htmlFor="browserName">Brauzer nomi</label>
              <div className="custom-dropdown" ref={dropdownRef}>
                <button
                  type="button"
                  className="dropdown-trigger"
                  onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                >
                  <span className={browserName ? 'selected' : 'placeholder'}>
                    {browserName || 'Brauzerni tanlang'}
                  </span>
                  <svg
                    className={`dropdown-arrow ${isDropdownOpen ? 'open' : ''}`}
                    width="20"
                    height="20"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="3"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <polyline points="6 9 12 15 18 9"></polyline>
                  </svg>
                </button>

                {isDropdownOpen && (
                  <div className="dropdown-menu">
                    {browsers.map((browser) => (
                      <div
                        key={browser}
                        className={`dropdown-item ${browserName === browser ? 'selected' : ''}`}
                        onClick={() => handleBrowserSelect(browser)}
                      >
                        {browser}
                        {browserName === browser && (
                          <svg
                            className="check-icon"
                            width="18"
                            height="18"
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="currentColor"
                            strokeWidth="3"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                          >
                            <polyline points="20 6 9 17 4 12"></polyline>
                          </svg>
                        )}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>

          <button
            onClick={handleSendMetrics}
            disabled={loading}
            className="btn-primary"
          >
            {loading ? 'Yuborilmoqda...' : 'Yuborish'}
          </button>
        </div>

        {success && (
          <div className="alert alert-success">
            <strong>Muvaffaqiyatli!</strong> Metrikalar yuborildi. Sahifa 3 sekunddan keyin yangilanadi...
          </div>
        )}

        {error && (
          <div className="alert alert-error">
            <strong>Xato:</strong> {error}
          </div>
        )}
      </div>
    </div>
  )
}

export default App
