"use client";
import Search from "./search";
import { SearchProvider } from "retake-search";

export default () => {
  return (
    <SearchProvider
      apiKey={process.env.RETAKE_API_KEY ?? ""}
      url={process.env.RETAKE_API_URL ?? ""}
    >
      <div className="w-full h-full p-12">
        <Search />
      </div>
    </SearchProvider>
  );
};
