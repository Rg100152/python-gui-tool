#!/usr/bin/env python3
"""
yaksha-proxy - Secure proxy server for CUI traffic inspection
Quack! This fine feathered friend has built a robust proxy system!
"""

import asyncio
import logging
from typing import Optional
import aiohttp
from aiohttp import web
import argparse
import time
from datetime import datetime
import sys
import socket
import ssl
from pathlib import Path

# ASCII Art Logo - Quack's Masterpiece!
LOGO = r"""
   _____       _   _       _____
  / ____|     | | | |     |  __ \
 | (___   ___ | |_| |__   | |__) | __ ___  ___ ___
  \___ \ / _ \| __| '_ \  |  ___/ '__/ _ \/ __/ __|
  ____) | (_) | |_| | | | | |   | | | (_) \__ \__ \
 |_____/ \___/ \__|_| |_| |_|   |_|  \___/|___/___/
"""

# Animation frames for startup
ANIMATION_FRAMES = [
    "🦆 Initializing proxy...",
    "🦆 Establishing secure tunnels...",
    "🦆 Inspecting packets...",
    "🦆 Ready to serve!",
]

class YakshaProxy:
    """Secure proxy server for CUI traffic inspection"""

    def __init__(self, host: str = "0.0.0.0", port: int = 8080,
                 upstream: str = "http://localhost:8000",
                 certfile: Optional[str] = None,
                 keyfile: Optional[str] = None):
        self.host = host
        self.port = port
        self.upstream = upstream
        self.certfile = certfile
        self.keyfile = keyfile
        self.app = web.Application()
        self.runner = None
        self.site = None
        self.logger = self._setup_logging()
        self._setup_routes()

    def _setup_logging(self) -> logging.Logger:
        """Configure logging for the proxy"""
        logger = logging.getLogger("yaksha-proxy")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _setup_routes(self) -> None:
        """Setup proxy routes"""
        self.app.router.add_route("*", "/{tail:.*}", self.handle_proxy)

    async def handle_proxy(self, request: web.Request) -> web.Response:
        """Handle proxy requests with inspection"""
        client_ip = request.remote
        method = request.method
        path = request.path
        headers = dict(request.headers)
        timestamp = datetime.now().isoformat()

        self.logger.info(f"[{timestamp}] {method} {path} from {client_ip}")

        # Inspect headers (example: block suspicious User-Agents)
        user_agent = headers.get('User-Agent', '')
        if "malicious" in user_agent.lower():
            self.logger.warning(f"Blocked suspicious request from {client_ip}")
            return web.Response(status=403, text="Forbidden")

        # Forward request to upstream server
        try:
            async with aiohttp.ClientSession() as session:
                # Prepare request to upstream
                req_headers = {k: v for k, v in headers.items()
                              if k.lower() not in ['host', 'content-length']}

                # Handle different HTTP methods
                if method in ("POST", "PUT", "PATCH"):
                    data = await request.read()
                    async with session.request(
                        method, f"{self.upstream}{path}",
                        headers=req_headers, data=data
                    ) as resp:
                        # Inspect response
                        response_data = await resp.read()
                        self.logger.info(
                            f"Response from upstream: {resp.status}"
                        )
                        return web.Response(
                            status=resp.status,
                            body=response_data,
                            headers=dict(resp.headers)
                        )
                else:
                    async with session.request(
                        method, f"{self.upstream}{path}",
                        headers=req_headers
                    ) as resp:
                        response_data = await resp.read()
                        self.logger.info(
                            f"Response from upstream: {resp.status}"
                        )
                        return web.Response(
                            status=resp.status,
                            body=response_data,
                            headers=dict(resp.headers)
                        )
        except Exception as e:
            self.logger.error(f"Proxy error: {str(e)}")
            return web.Response(status=502, text="Bad Gateway")

    async def start(self) -> None:
        """Start the proxy server"""
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()

        if self.certfile and self.keyfile:
            ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            ssl_context.load_cert_chain(self.certfile, self.keyfile)
            self.site = web.TCPSite(
                self.runner, self.host, self.port, ssl_context=ssl_context
            )
            self.logger.info(f"Starting HTTPS proxy on {self.host}:{self.port}")
        else:
            self.site = web.TCPSite(self.runner, self.host, self.port)
            self.logger.info(f"Starting HTTP proxy on {self.host}:{self.port}")

        await self.site.start()
        self.logger.info("Proxy server started successfully!")

    async def stop(self) -> None:
        """Stop the proxy server"""
        if self.site:
            await self.site.stop()
        if self.runner:
            await self.runner.cleanup()
        self.logger.info("Proxy server stopped")

def display_animation() -> None:
    """Display startup animation"""
    for frame in ANIMATION_FRAMES:
        print(f"\r{frame}", end="", flush=True)
        time.sleep(0.5)
    print("\n")

def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="yaksha-proxy - Secure proxy server")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8080, help="Port to listen on")
    parser.add_argument("--upstream", default="http://localhost:8000",
                       help="Upstream server to proxy to")
    parser.add_argument("--certfile", help="Path to SSL certificate file")
    parser.add_argument("--keyfile", help="Path to SSL private key file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()

async def main() -> None:
    """Main entry point"""
    args = parse_args()

    # Display our beautiful logo
    print(LOGO)
    display_animation()

    # Create and start proxy
    proxy = YakshaProxy(
        host=args.host,
        port=args.port,
        upstream=args.upstream,
        certfile=args.certfile,
        keyfile=args.keyfile
    )

    if args.verbose:
        proxy.logger.setLevel(logging.DEBUG)

    try:
        await proxy.start()
        while True:
            await asyncio.sleep(3600)  # Keep running
    except KeyboardInterrupt:
        print("\nQuack! Shutting down gracefully...")
        await proxy.stop()
    except Exception as e:
        print(f"\nQuack! Error: {str(e)}")
        await proxy.stop()
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nQuack! Exiting...")
        sys.exit(0)
